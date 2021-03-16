import React from "react";
import { connect } from "react-redux";

import FormLabel from '@material-ui/core/FormLabel';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormHelperText from '@material-ui/core/FormHelperText';
import Checkbox from '@material-ui/core/Checkbox';
import { withStyles } from '@material-ui/core/styles';

import { Collapse, Radio, Button } from 'antd';
import Slider from '../PriceRange'

import FeatureHome from "../FeatureHome/index"
import PaginationButtons from "../Pagination/index"

import { allProductsCStoreActions } from './store'

import style from './style.local.scss';


const useStyles = theme => ({
  formControl: {
    margin: theme.spacing(0),
  },
});
const { Panel } = Collapse;
export default
@connect((state, props) => ({
  allProductsCStore: state.allProductsCStore
}))
@withStyles(useStyles)
class AllProducts extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      range_values: [1, 30]
    }
  }

  UNSAFE_componentWillMount(){
    var url = window.location.pathname
    var url_table = url.split("/")
    var product_menu = url_table.slice(-1)[0]

    console.log("VOILA LE PROPS PRODUCT ICI", product_menu)

    this._fetchProducts(product_menu)
  }

  _fetchProducts(params){
    this.props.dispatch(allProductsCStoreActions.setLoading(true))

    const url = `/api/products/?menu=${params}`

    window.axios
    .get(`${url}`)
    .then(response => {
      var products = response.data

      this.props.dispatch(allProductsCStoreActions.setProducts(products))
      setTimeout(() => {
        this.props.dispatch(allProductsCStoreActions.setLoading(false))
      }, 2000);
    })
    .catch(
      error => {
        console.error("Errrorr", error)
        this.props.dispatch(allProductsCStoreActions.setLoading(false))
      }
    )
  }

  handleChange = (event, newValue) => {
    this.setState({
      range_values: newValue
    })
  };

  valuetext(value) {
    return `${value}°C`;
  }


  render() {
    const { products } = this.props.allProductsCStore
    const { classes } = this.props;
    const marks = [
      {
        value: 0,
        label: '0',
      },
      {
        value: 50,
        label: '50k',
      },
      {
        value: 100,
        label: '100k',
      },
    ];

    return (
      //<!-- Document Wrapper -->
      <div className="" style={{ backgroundColor: "#fff" }}>
        <section style={{ paddingTop: 40, paddingBottom: 40  }}>
          <div className="container">
            <div className="row">
              <div className="col-sm-3">
                <div className={style.product_list_filter_block}>
                  <div className="col-sm-12" style={{ padding: 0 }}>
                    <Collapse
                      bordered={false}
                      showArrow={false}
                      defaultActiveKey={['1', '2', '3', '4', '5']}
                      expandIconPosition="right"
                      style={{ backgroundColor: "#fff", padding: 0 }}
                    >
                      <Panel header="Catégorie" key="1">
                        <FormControl component="fieldset" className={classes.formControl}>
                          <FormGroup>
                            <FormControlLabel
                              control={<Checkbox name="accessory" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Accéssoires"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="beauty" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Beauté"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="jewel" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Bijoux"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="shoes" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Chaussures"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="bags" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Sacs"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="clothes" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Vêtements"
                              className={style.checkBoxControlStyle}
                            />
                          </FormGroup>
                        </FormControl>
                      </Panel>
                      <Panel header="Groupe" key="2">
                        <FormControl component="fieldset" className={classes.formControl}>
                          <FormGroup>
                            <FormControlLabel
                              control={<Checkbox name="bracelet" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Bracelet"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="echarpe" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Echarpe"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="escarpin" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Escarpin"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="parfume" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Parfum"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="wallet" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Porte monnaie"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="dress" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }}  style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Robe"
                              className={style.checkBoxControlStyle}
                            />
                          </FormGroup>
                        </FormControl>
                      </Panel>
                      <Panel header="Interval de prix" key="3">
                        <Slider
                          value={this.state.range_values}
                          onChange={this.handleChange}
                          getAriaValueText={this.valuetext}
                          step={5}
                          marks={marks}
                        />
                      </Panel>
                      <Panel header="Tailles" key="4">
                        <div>
                          <Radio.Group defaultValue="xl" buttonStyle="solid" >
                            <Radio.Button value="s" style={{ marginRight: 10, marginBottom: 5 }}>S</Radio.Button>
                            <Radio.Button value="m" style={{ marginRight: 10, marginBottom: 5 }}>M</Radio.Button>
                            <Radio.Button value="l" style={{ marginRight: 10, marginBottom: 5 }}>L</Radio.Button>
                            <Radio.Button value="xl" style={{ marginRight: 10, marginBottom: 5 }}>XL</Radio.Button>
                            <Radio.Button value="xxl" style={{ marginRight: 10, marginBottom: 5 }}>XXL</Radio.Button>
                          </Radio.Group>
                        </div>
                      </Panel>
                      <Panel header="Couleur" key="5">
                        <div>
                          {/*<Radio.Group defaultValue="black" buttonStyle="solid">
                            <Radio.Button value="black" style={{ marginRight: 10, marginBottom: 5, backgroundImage: "url('/static/images/logo.jpg')", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="blue" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#03a9f4 !important", width: 30, height: 30 }}>
                            </Radio.Button>
                            <Radio.Button value="brown" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#77470c !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="gold" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#f1c907 !important", width: 30, height: 30 }}></Radio.Button>

                            <Radio.Button value="gray" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#9c9c9c !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="green" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#4caf50 !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="ivoryCream" color="#f7f7ba" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#f7f7ba !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="orange" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "orange !important", width: 30, height: 30 }}></Radio.Button>

                            <Radio.Button value="pink" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "pink !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="chroma" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#000 !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="multi" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#c0c0c0 !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="purple" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "purple !important", width: 30, height: 30 }}></Radio.Button>

                            <Radio.Button value="red" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "red !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="beige" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "#f7edba !important", width: 30, height: 30 }}></Radio.Button>
                            <Radio.Button value="white" style={{ marginRight: 10, marginBottom: 5, backgroundColor: "white !important", width: 30, height: 30 }}></Radio.Button>
                          </Radio.Group>*/}
                        </div>
                      </Panel>
                    </Collapse>
                  </div>
                </div>
              </div>
              <div className="col-sm-9 padding-right" style={{ marginBottom: 20 }}>
                <div className="row" style={{ paddingBottom: 10, borderBottom: "1px solid lightgray" }}>
                  <div className="col-sm-9" style={{ paddingLeft: 0 }}>
                    <span style={{ fontSize: "1.2em", paddingLeft: "10px" }}>32 Produits trouvés</span>
                  </div>
                  <div className="col-sm-3"></div>
                </div>
                <FeatureHome products={ products } />
                { products.length >= 9 && <PaginationButtons />}
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}
