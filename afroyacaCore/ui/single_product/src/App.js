import React, { Component } from "react";
import { connect } from "react-redux";

import SingleProduct from './components/single_product/index'
import { clearUser, initAxios, getUser } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'single_product',
});


initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
    <StylesProvider generateClassName={generateClassName}>
        <div>
          <SingleProduct />
        </div>
    </StylesProvider>

    );
  }

}
