import React, { Component } from "react";
import { connect } from "react-redux";

import MyBox from './components/my_box/index'
import { initAxios } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'my_box',
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
          <MyBox />
        </div>
    </StylesProvider>

    );
  }

}
