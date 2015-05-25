var path = require('path');

module.exports = {
    entry: './aligot/static/src/index',
    output: {
        path: path.join(__dirname, 'aligot/static'),
        filename: 'aligot.js'
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                include: path.join(__dirname, 'aligot/static/src'),
                loader: 'babel',
                query: {
                    optional: ['runtime'],
                    stage: 1
                }
            }
        ]
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    }
};
