import React, { Component } from "react";
import { connect } from "react-redux";

import HorizontalScroll from './components/horizontal_scroll/index'
import { clearUser, initAxios } from "./utils/auth_utils";


initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
        <div>
          <HorizontalScroll />
        </div>

    );
  }

}
