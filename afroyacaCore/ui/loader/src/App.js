import React, { Component } from "react";
import { connect } from "react-redux";

import Loader from './components/loader/index'
import { clearUser, initAxios } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'loader',
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
          <Loader />
        </div>
      </StylesProvider>

    );
  }

}
