const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
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
		path: path.resolve(__dirname, 'lenticular_cloud/static'),
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
        "test": /\.(svg|eot|woff|woff2|ttf)$/,
        type: 'asset/resource',
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
			new CssMinimizerPlugin({
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
	],
  // workaround for qrcode-svg
  "resolve": {
    "fallback": {
      "fs": false,
    }
  }
};
