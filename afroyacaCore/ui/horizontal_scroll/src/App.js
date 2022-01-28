import React, { Component } from "react";
import { connect } from "react-redux";

import HorizontalScroll from './components/horizontal_scroll/index'
import { clearUser, initAxios } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'horizontal_scroll',
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
          <HorizontalScroll />
        </div>
    </StylesProvider>

    );
  }

}
