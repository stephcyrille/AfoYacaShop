import React, { Component } from "react";
import { connect } from "react-redux";

import AllProducts from './components/all_products/index'
import { clearUser, initAxios, getUser } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'products',
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
          <AllProducts />
        </div>
    </StylesProvider>

    );
  }

}
