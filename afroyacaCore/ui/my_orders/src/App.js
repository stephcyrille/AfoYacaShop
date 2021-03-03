import React, { Component } from "react";
import { connect } from "react-redux";

import { clearUser, initAxios, getUser } from "./utils/auth_utils";


initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
        <div>
          <h1>Test my_orders</h1>
        </div>

    );
  }

}
