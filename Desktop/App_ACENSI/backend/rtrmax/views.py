from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from django.template import loader

def index(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    symbol = request.GET.get('symbol')
    market_index = request.GET.get('market_index')
    
    with connection.cursor() as cursor:
        query = ("""SELECT DISTINCT symbol FROM Underlying WHERE marketid = %s order by symbol """) 
        cursor.execute(query, [market_index])
        symbols = [row[0] for row in cursor.fetchall()]  # Récupération des symboles

    with connection.cursor() as cursor:
        query2 = ("""
            SELECT TOP 15 l.symbol, s.spotvalue, m.date 
            FROM Marketdata AS m
            JOIN Underlyingmarketdata AS u ON m.marketdataid = u.marketdataid
            JOIN Underlying AS l ON u.underlyingid = l.underlyingid
            JOIN Spotmarketdata AS s ON m.marketdataid = s.marketdataid
            JOIN Market AS d ON d.marketid = l.marketid
            WHERE l.symbol = %s
        """)
        
        params = [symbol]
        
        if start_date:
            query2 += " AND m.date >= %s"  # Filter by start date
            params.append(start_date)

        if end_date:
            query2 += " AND m.date <= %s"  # Filter by end date
            params.append(end_date)
            
        cursor.execute(query2, params)
        results = cursor.fetchall()

        # Récupération des données (index corrigés)
        spot_values = [row[1] for row in results]
        dates = [row[2].strftime('%Y-%m-%d') for row in results]  # Formatage des dates

    zipped_data = list(zip(spot_values, dates))

    if request.is_ajax():
        response_data = {
            'chartLabels': dates,
            'chartData': spot_values,
            'chartSymbol': symbol,
            'treeData': [
                {
                    "text": symbol,
                    "children": [
                        {
                            "text": "SpotValue",
                            "children": [
                                {"text": date, "children": [{"text": value, "icon": "jstree-calendar-icon"}]}
                                for value, date in zipped_data
                            ]
                        }
                    ]
                }
            ],
            'zippedData': zipped_data
        }
        return JsonResponse(response_data)

    context = {
        "labels": dates,
        "data": spot_values,
        "symbol": symbol,
        "symbols": symbols,
        'zipped_data': zipped_data,
    }

    return render(request, "rtrmax/index.html", context)




def test(request):
    context = {
        #"Cultures": Culture.objects.all()
    }
    return render(request, "rtrmax/test.html", context)

def nindex(request):
    context = {
        #"Cultures": Culture.objects.all()
    }
    return render(request, "rtrmax/new_index.html", context)
