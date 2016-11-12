
var subs ={"blogger": 2,
"robotics": 0,
"Bitcoin": 2,
"AirBnB": 4,
"Music": 6,
"audiobooks": 4,
"askphilosophy": 35,
}


var arr1 = [];
var arr2 = [];
console.log(arr1)
for (var keys in subs){
	arr1.push(keys)
	arr2.push(subs[keys])
}


var ctx = document.getElementById("canvasId").getContext("2d");
                        
var graph = new BarGraph(ctx);

graph.margin = 2;
graph.width = 450;
graph.height = 150;
graph.xAxisLabelArr = arr1;
graph.update(arr2);



