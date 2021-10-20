var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const WebpackBundleAnalyzer = require("webpack-bundle-analyzer").BundleAnalyzerPlugin;

module.exports = {
  mode: "production",

  entry: {
    my_box: './ui/my_box/src/index.js',
    my_orders: './ui/my_orders/src/index.js',
    loader: './ui/loader/src/index.js',
    mobile_navbar: './ui/mobile_navbar/src/index.js',
    single_product: './ui/single_product/src/index.js',
    all_products: './ui/all_products/src/index.js',
    horizontal_scroll: './ui/horizontal_scroll/src/index.js'
  },
  output: {
    path: path.join(__dirname, "../static/ui/"),
    filename: "[name].min.js"
  },

  plugins: [
    new BundleTracker({filename: './webpack_stats/webpack-stats.json'}), new WebpackBundleAnalyzer()
  ],

  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react"],
          },
        },
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
              modules: true
              // localIdentName: "[local]___[hash:base64:5]"
            }
          },
          {
            loader: "sass-loader",
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
  },


  optimization: {
    splitChunks: {
      cacheGroups: {
        vendors: {
          test: /[\\/]node_modules[\\/]/, ///< put all used node_modules modules in this chunk
          name: "vendor", ///< name of bundle
          chunks: "all", ///< type of code to put in this bundle
          filename: "vendors.min.js"
        }
      }
    }
  },


  resolve: {
    extensions: ['.js', '.jsx', '.json']
  },
};
