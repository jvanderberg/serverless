function getIterations(_ref) {
	//This is a test comment
	var start = Number(_ref.start),
		stop = Number(_ref.stop),
		width = Number(_ref.width),
		offsetx = Number(_ref.offsetx),
		offsety = Number(_ref.offsety),
		panx = Number(_ref.panx),
		pany = Number(_ref.pany),
		zoom = Number(_ref.zoom),
		maxIterations = _ref.maxIterations;
	console.log(maxIterations);
	// Convert the screen coordinate to a fractal coordinate
	var iterationsArray = [];
	for (var i = start; i < stop; i++) {
		var x = i % width;
		var y = Math.floor(i / width);
		var x0 = (x + offsetx + panx) / zoom;
		var y0 = (y + offsety + pany) / zoom;

		var a = 0;
		var b = 0;
		var rx = 0;
		var ry = 0;
		var iterations = 0;
		while (iterations <= maxIterations && rx * rx + ry * ry <= 4) {
			rx = a * a - b * b + x0;
			ry = 2 * a * b + y0;
			a = rx;
			b = ry;
			iterations++;
		}
		iterationsArray.push(iterations);
	}
	//return _ref;
	return iterationsArray;
}

exports.handler = (event, context, callback) => {
	var result = getIterations(event.params.querystring);
	callback(null, result);
};
