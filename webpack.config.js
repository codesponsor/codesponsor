const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: [
    './assets/js/application.js',
    './assets/styles/application.scss',
  ],
  devtool: 'inline-source-map',
  output: {
    path: path.resolve(__dirname, 'static/bundles'),
    filename: '[name].js',

    // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
    publicPath: 'http://localhost:8000/static/bundles/'
  },
  module: {
    rules: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['env'],
              plugins: ['transform-class-properties']
            },
          },
        ],
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].css',
              outputPath: ''
            }
          },
          {
            loader: 'extract-loader'
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader'
          },
          {
            loader: 'sass-loader'
          }
        ]
      }
    ]
  },
  plugins: [
  ],
  resolve: {
    alias: {
      modulesDirectories: path.resolve(__dirname, 'node_modules')
    },
    extensions: ['.js']
  }
};

if (process.env.NODE_ENV === 'production') {
  module.exports.plugins = [
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
    new webpack.optimize.OccurenceOrderPlugin()
  ]
} else {
  module.exports.devtool = '#source-map'
}