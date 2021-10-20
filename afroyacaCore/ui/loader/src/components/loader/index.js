import React from "react";
import { connect } from "react-redux";
import { PulseLoader } from 'react-spinners';
import _ from "underscore";

import { loaderCStoreActions } from './store'
import './style.local.css';



export default
@connect((state, props) => ({
  loaderCStore: state.loaderCStore
}))
class Loader extends React.Component {

  UNSAFE_componentWillMount(){
    this.props.dispatch(loaderCStoreActions.setLoading(true))

    setTimeout(() => {
      this.props.dispatch(loaderCStoreActions.setLoading(false))
    }, 2000);
  }


  render() {
    const { loading } = this.props.loaderCStore

    return (
      //<!-- Document Wrapper -->
      <div className="" style={{ backgroundColor: "white" }}>
        { loading ? (
            <div className='home-loading'>
              <div className='reverse-spinner'>
                <PulseLoader
                  color={'#FE980F'}
                  loading={loading}
                />
              </div>
            </div>)
          : ''
        }
      </div>
    );
  }
}
