var path = require('path');
var webpack = require('webpack');

module.exports = {
    devtool: 'eval',
    entry: [
        './aligot/static/src/index'
    ],
    output: {
        path: path.join(__dirname, 'aligot/static'),
        filename: 'aligot.js',
        publicPath: '/aligot/static/src/'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin()
    ],
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    module: {
        loaders: [{
            test: /\.jsx?$/,
            loaders: ['react-hot', 'babel'],
            include: path.join(__dirname, 'aligot/static/src')
        }]
    }
};
