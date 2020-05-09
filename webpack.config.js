const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack')

var debug=false;

module.exports = {
	entry: [
		'./browser_app/index.js',
		'./browser_app/style.scss'
	],
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'static'),
	},
	devtool: "source-map",
	module: {
		rules: [
			{
				"test": /\.tsx?$/,
				"exclude": /node_modules/,
				"use": {
					"loader": "ts-loader",
					"options": {
						"transpileOnly": true
					}
				}
			},
			{
				test: /\.s[ac]ss$/i,
				use:[
					MiniCssExtractPlugin.loader,
					'css-loader',
					'sass-loader'
				]
			},
			{
				"test": /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				"use": {
					"loader": "url-loader?limit=10000&mimetype=application/font-woff",
					"options": {
						name: '[path][name].[ext]',
					},
				}
			},
			{
				"test": /\.(ttf|eot|svg|gif)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
				"use": [
					"file-loader"
				]
			},
			{
				test: /\.css$/,
				use: ['style-loader', 'css-loader'],
			}
		]
	},
	"optimization": {
		minimize: !debug,
		minimizer: [
			new TerserPlugin({
				include: /\.js$/
			}),
			new OptimizeCSSAssetsPlugin({
				include: /\.css$/
			})
		]
	},
	"plugins": [
		new webpack.ProvidePlugin({
			$: "jquery",
			jQuery: "jquery"
		}),
		new MiniCssExtractPlugin(),
	]
};
