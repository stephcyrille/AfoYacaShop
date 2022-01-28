import React from "react";
import { connect } from "react-redux";
import { PulseLoader } from 'react-spinners';

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
}, { index : 1 });
const { Panel } = Collapse;
export default
@connect((state, props) => ({
  allProductsCStore: state.allProductsCStore
}))
@withStyles(useStyles)
class AllProducts extends React.Component {
  state = {
    range_values: [1, 30],
    /* TODO rename it to Category_filter */
    filterList: [
      {
        id: 11,
        name: "Accéssoires",
        value: "accessories"
      },
      {
        id: 12,
        name: "Beauté",
        value: "beauties"
      },
      {
        id: 13,
        name: "Bijoux",
        value: "jewels"
      },
      {
        id: 14,
        name: "Chaussures",
        value: "shoes"
      },
      {
        id: 15,
        name: "Sacs",
        value: "bags"
      },
      {
        id: 16,
        name: "Vêtements",
        value: "cloths"
      }
    ],
    searchLists: this.props.allProductsCStore.products,
    activeFilter: []
  };

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

  handleCheckboxClick(e){
    console.log(`Checkbox name: ${e.target.name} is checked:${e.target.checked}`)

    const { products } = this.props.allProductsCStore

    var result = products.filter(function(x) {
        return x.category==e.target.name
    })

    this.props.dispatch(allProductsCStoreActions.setLoading(true))

    if(e.target.checked){
      this.props.dispatch(allProductsCStoreActions.setFilter(result))
      setTimeout(() => {
        this.props.dispatch(allProductsCStoreActions.setLoading(false))
      }, 2000);
    } else {
      this.props.dispatch(allProductsCStoreActions.unSetFilter())
      setTimeout(() => {
        this.props.dispatch(allProductsCStoreActions.setLoading(false))
      }, 2000);
    }

    console.log(`Initial products array`, products)
    console.log(`New products array :`, result)
  }

  valuetext(value) {
    return `${value}°C`;
  }

  onFilterChange(filter) {
    console.log("The filter is", filter)
    const { filterList, activeFilter } = this.state;
    if (filter === "ALL") {
      if (activeFilter.length === filterList.length) {
        this.setState({ activeFilter: [] });
      } else {
        this.setState({ activeFilter: filterList.map(filter => filter.value) });
      }
    } else {
      if (activeFilter.includes(filter)) {
        const filterIndex = activeFilter.indexOf(filter);
        const newFilter = [...activeFilter];
        newFilter.splice(filterIndex, 1);
        this.setState({ activeFilter: newFilter });
        console.log("New filter list", newFilter)
      } else {
        this.setState({ activeFilter: [...activeFilter, filter] });
      }
    }
  }



  render() {
    const { products, loading, filter, filtered_products } = this.props.allProductsCStore
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
    var productList = filter ? filtered_products : products

    const { filterList, activeFilter } = this.state;
    let filteredList;
    if (
      activeFilter.length === 0 ||
      activeFilter.length === filterList.length
    ) {
      filteredList = this.state.searchLists;
    } else {
      filteredList = this.state.searchLists.filter(item =>
        this.state.activeFilter.includes(item.type)
      );
    }


    return (
      //<!-- Document Wrapper -->
      <div className="" style={{ backgroundColor: "#fff" }}>
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
                              control={
                                <Checkbox
                                  name="ALL"
                                  id="all"
                                  onClick={() => this.onFilterChange("ALL")}
                                  checked={activeFilter.length === filterList.length}
                                  iconStyle={{ fill: "#ddaa44" }}
                                  style={{ color: "#ddaa44", padding: "5px 10px" }} />
                              }
                              label="Tous"
                              className={style.checkBoxControlStyle}
                            />


                            {this.state.filterList.map(filter => (
                              <FormControlLabel
                                control={
                                  <Checkbox
                                    name="accessories"
                                    id={filter.id}
                                    checked={activeFilter.includes(filter.value)}
                                    onClick={() => this.onFilterChange(filter.value)}
                                    iconStyle={{ fill: "#ddaa44" }}
                                    style={{ color: "#ddaa44", padding: "5px 10px" }} />
                                }
                                label={filter.name}
                                className={style.checkBoxControlStyle}
                              />
                            ))}
                          </FormGroup>
                        </FormControl>
                      </Panel>

                      <Panel header="Groupe" key="2">
                        <FormControl component="fieldset" className={classes.formControl}>
                          <FormGroup>
                            <FormControlLabel
                              control={<Checkbox name="bracelet" value="bracelet" iconStyle={{ fill: "#ddaa44" }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Bracelet"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="echarpe" value="echarpe" iconStyle={{ fill: "#ddaa44" }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Echarpe"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="escarpin" value="escarpin" iconStyle={{ fill: "#ddaa44" }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Escarpin"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="parfume" value="parfume" iconStyle={{ fill: "#ddaa44" }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Parfum"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="wallet" value="wallet" iconStyle={{ fill: "#ddaa44" }} inputStyle={{ color: '#ddaa44' }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
                              label="Porte monnaie"
                              className={style.checkBoxControlStyle}
                            />
                            <FormControlLabel
                              control={<Checkbox name="dress" value="dress" iconStyle={{ fill: "#ddaa44" }} style={{ color: "#ddaa44", padding: "5px 10px" }} />}
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
                    <span style={{ fontSize: "1.2em", paddingLeft: "10px" }}>{ productList.length } Produits trouvé{ productList.length > 1 ? 's': '' }</span>
                  </div>
                  <div className="col-sm-3"></div>
                </div>
                <FeatureHome products={ productList } />
                { products.length >= 9 && <PaginationButtons />}
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}
