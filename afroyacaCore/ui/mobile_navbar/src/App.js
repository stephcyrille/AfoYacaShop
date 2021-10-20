import React, { Component } from "react";
import { connect } from "react-redux";

import PersistentDrawerLeft from './components/mobile_navbar/index'
import { clearUser, initAxios } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'navbar',
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
          <PersistentDrawerLeft />
        </div>
      </StylesProvider>

    );
  }

}
