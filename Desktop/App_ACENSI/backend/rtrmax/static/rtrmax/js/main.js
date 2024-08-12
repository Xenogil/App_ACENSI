// var colonne1 = document.getElementById('colonne1');
// var colonne2 = document.getElementById('colonne2');
// var colonne3 = document.getElementById('colonne3');
// var element1 = document.getElementById('element1');
// var element2 = document.getElementById('element2');
// var element3 = document.getElementById('element3');
// $(function() {
//     var treeData = JSON.parse($("#treeData").html()); // Récupérer les données JSON

//     $('#jstreeContainer').jstree({
//         'core': {
//             'data': treeData, // Utiliser les données JSON directement
//             'themes': {
//                 'icons': true // Activer les icônes
//             }
//         },
//         'plugins': ['themes', 'types'], // Ajout du plugin "types"
//         'types': {
//             'calendar-icon': { // Définition du type "calendar-icon"
//                 'icon': 'jstree-calendar-icon'
//             }
//         }
//     });

// //     var config = {
// //     content: [{
// //         type: 'column',
// //         content:[{
// //             type: 'component',
// //             componentName: 'testComponent',
// //             componentState: { label : 1, elementId: 'win1' }
// //         },{
// //             type: 'column',
// //             content:[{
// //                 type: 'component',
// //                 componentName: 'testComponent',
// //                 componentState: { label : 2, elementId: 'win2' }
// //             },{
// //                 type: 'component',
// //                 componentName: 'testComponent',
// //                 componentState: {label : 3, elementId: 'win3' }
// //             }]
// //         }]
// //     }]
// // };

// // var myLayout = new GoldenLayout( config );

// // myLayout.registerComponent( 'testComponent', function( container, componentState ){
// //     var elementId = componentState.elementId;
// //     var divElement = document.getElementById(elementId);
// //     if (divElement) {
// //         var contentId = "win" + componentState.label;
// //         var contentElement = divElement.querySelector('#' + contentId);
// //         if (contentElement) {
// //             var contentHtml = contentElement.innerHTML;
// //             container.getElement().append(contentHtml);
// //         }
// //     }
// // });

// // myLayout.init();
// });

// var addMenuItem = function (title, text) {
//   var element = $("<li>" + text + "</li>");
//   $("#menuContainer").append(element);

//   var newItemConfig = {
//     title: title,
//     type: "component",
//     componentName: "example",
//     componentState: { text: text },
//   };

//   element.click(function () {
//     myLayout.root.contentItems[0].addChild(newItemConfig);
//   });
// };

// addMenuItem("Add me!", "You've added me!");
// addMenuItem("Me too!", "You've added me too!");
