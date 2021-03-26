var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
  mode: "development",

  entry: {
    my_orders: './ui/my_orders/src/index.js',
    loader: './ui/loader/src/index.js',
    mobile_navbar: './ui/mobile_navbar/src/index.js',
    all_products: './ui/all_products/src/index.js',
    single_product: './ui/single_product/src/index.js',
    my_box: './ui/my_box/src/index.js',
    horizontal_scroll: './ui/horizontal_scroll/src/index.js'
  },
  output: {
    path: path.join(__dirname, "static/dist"),
    filename: "[name]-[hash].js"
  },

  devtool: "source-map",

  plugins: [
    new BundleTracker({filename: './webpack_stats/webpack-stats.json'})
  ],

  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: ["style-loader", "css-loader"]
      },
      {
        test: /\.(scss|sass)$/,

        use: [
          {
            loader: "style-loader"
          },
          {
            loader: "css-loader",
            options: {
              importLoaders: 1,
              modules: true,
              sourceMap: process.env.NODE_ENV !== "production",
              // localIdentName: "[local]___[hash:base64:5]"
            }
          },
          {
            loader: "sass-loader",
            options: {
              sourceMap: process.env.NODE_ENV !== "production"
            }
          }
        ]
      },
      {
        test: /\.(png|jpg|gif|svg)$/i,
        use: [
          {
            loader: "url-loader",
            options: {
              limit: 8192
            }
          }
        ]
      }
    ]
  }
  ,
  resolve: {
    modules: [
                'node_modules',
                path.resolve(__dirname, './ui/my_orders/src'),
                path.resolve(__dirname, './ui/loader/src'),
                path.resolve(__dirname, './ui/horizontal_scroll/src'),
                path.resolve(__dirname, './ui/single_product/src'),
                path.resolve(__dirname, './ui/all_products/src'),
                path.resolve(__dirname, './ui/my_box/src'),
                path.resolve(__dirname, './ui/mobile_navbar/src')
             ],
    extensions: ['.js', '.jsx', '.json'],
    alias: {
      "app-js": path.resolve(__dirname, './src')
    }
  },
};
