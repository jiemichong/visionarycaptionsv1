const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  mode: "production",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.js$/i,
        include: path.resolve(__dirname, "src"),
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/i,
        include: path.resolve(__dirname, "src"),
        use: ["style-loader", "css-loader", "postcss-loader"],
      },
    ],
  },
  devServer: {
    contentBase: path.resolve(__dirname, "dist"),
    watchContentBase: true,
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        { from: "data/*.json" },
      ],
    }),
  ],
};