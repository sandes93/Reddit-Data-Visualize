
var subs ={
"Transhuman": 0,"RationalPsychonaut": 19,"DMT": 27,"philosophy": 238,"politics": 0,"philosophy": 6806,

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



