import React from "react";
import { connect } from "react-redux";
import { withTranslation } from 'react-i18next';
import _ from "underscore";
import { BeatLoader, RotateLoader } from 'react-spinners';
import { Collapse } from 'antd';
import {
  EmailShareButton,
  FacebookShareButton,
  WhatsappShareButton,

  FacebookIcon,
  EmailIcon,
  WhatsappIcon
} from "react-share";
import { reduxForm, Field, propTypes as reduxFormPropTypes } from "redux-form";
import { Button, TextField, Paper } from "@material-ui/core";
import Grow from '@material-ui/core/Grow';
import Dialog from '../Snippets/MyDialog'

import { saveCartSession } from '../../utils/session_utils'
import { getCookie } from '../../utils/auth_utils'

import './style.local.css';

// Stores and stores actions importation
import { singleProductCStoreActions } from "./store";


const { Panel } = Collapse;


export default
@withTranslation()
@connect((state, props) => ({
  singleProductCStore: state.singleProductCStore,
}))
@reduxForm({ form: "addToCartForm", enableReinitialize: true })
class SingleProduct extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      dialogOpen: false,
      quantity: 0,
      product: {}, // Product pass to model when with click onaddToCart button
    }
  }


  UNSAFE_componentWillMount(){
    var url = window.location.pathname
    var url_table = url.split("/")
    var slug = url_table.slice(-1)[0]

    console.log("VOILA LE PROPS SLUG ICI", slug)

    this.props.dispatch(singleProductCStoreActions.setProductSlug(slug))
    this._fetchSingleProduct(slug)
    this.props.change('quantity', this.props.singleProductCStore.quantity);
  }


  _fetchSingleProduct(slug){
    const { variety_id } = this.props.singleProductCStore
    this.props.dispatch(singleProductCStoreActions.setLoading(true))

    window.axios
    .get(`/api/products/${slug}/`)
    .then(response => {
      var product = response.data
      // console.log("Product single fetched!!!!!!!!!!!!", product)
      this.props.dispatch(singleProductCStoreActions.setSingleProduct(product))
      this.props.dispatch(singleProductCStoreActions.setStockQuantity(product.varieties[variety_id].quantity))
      setTimeout(() => {
        this.props.dispatch(singleProductCStoreActions.setLoading(false))
      }, 2000);
    })
    .catch(
      error => {
        console.error("Errrorr", error)
        setTimeout(() => {
            this.props.dispatch(singleProductCStoreActions.setLoading(false))
          }, 2000);
        //window.location.href = `/`;
      }
    )
  }


  _handleAddToCart(formValues){
    console.log("Product added to cart!!!!!!!!!!!!", formValues.quantity)
    // Call api to adding cart item on cart now
    this.props.dispatch(singleProductCStoreActions.setLoading(true))

    const { stock_quantity, single_product, variety_id , product_slug } = this.props.singleProductCStore
    var result = stock_quantity - formValues.quantity

    this.handleSetDialogOpen(single_product, formValues.quantity)

    this.props.dispatch(singleProductCStoreActions.setStockQuantity(result))

    if (result < 0){
      this.props.change('quantity', 0);
    } else {

      var cart_item = {
        variety : single_product.varieties[variety_id].id,
        quantity : formValues.quantity
      }

      var csrftoken = getCookie('csrftoken');
      var headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
      }

      window.axios
      .post(`/api/cart/add_item/`, {data: cart_item}, {headers: headers})
      .then(response => {
        // Toggle state of navbar to true an set time out to reback to false after 3000
        this.props.dispatch(singleProductCStoreActions.setLoading(false))
      })
      .catch(err => {
        this.props.dispatch(singleProductCStoreActions.setLoading(false))
        console.error("Error when adding item to cart", err)
      })

      this.props.change('quantity', 1);
      // Updating product list because the quantity of product variety decrease
      this._fetchSingleProduct(product_slug)
    }
  }


  _handleAddToWhishList(){
    console.log("Product added to whishlist!!!!!!!!!!!!")
  }

  _handleAddQuantity(){
    var qty = this.props.singleProductCStore.quantity + 1

    this.props.change('quantity', qty);
    this.props.dispatch(singleProductCStoreActions.setProductQuantity(qty))
  }

  _handleRemoveQuantity(){
    if(this.props.singleProductCStore.quantity > 1 ){
      var qty = this.props.singleProductCStore.quantity - 1

      this.props.change('quantity', qty);
      this.props.dispatch(singleProductCStoreActions.setProductQuantity(qty))
    }
  }

  _handleChangeVariety(id, quantity){
    this.props.dispatch(singleProductCStoreActions.setThumbnailPictureKey(0))
    this.props.dispatch(singleProductCStoreActions.setPicLoading(true))
    setTimeout(()=> {
      this.props.dispatch(singleProductCStoreActions.setPicLoading(false))
      // console.log("BBBBBBBBBAAAAAAAAAAMMMMMMMMMMMMMMMMMMMMMMMMM", id)
      this.props.dispatch(singleProductCStoreActions.setVarietyID(id))
    }, 2000)
    this.props.dispatch(singleProductCStoreActions.setStockQuantity(quantity))
    this.props.change('quantity', 1);
    this.props.dispatch(singleProductCStoreActions.setProductQuantity(1))
    console.log("Stock quantity ",quantity)
  }

  _handleChangeVarietyImage(key){
    console.log("Image changed! key is: ", key)
    this.props.dispatch(singleProductCStoreActions.setThumbnailPictureKey(key))
  }


  handleSetDialogOpen(element, qty){
    this.setState({
      dialogOpen: true,
      product: element,
      quantity: qty,
    })
  }

  handleSetDialogClose(){
    this.setState({
      dialogOpen: false,
      product: {},
      quantity: 0,
    })

    // Refresh the page
    window.location.reload()
  }

  handleGotoCart(){
    this.handleSetDialogClose()
    window.location.href = `/shop/cart/my`;
  }




  render() {
    const { quantity, stock_quantity, loading, single_product, variety_id, pic_loading, thumbnail_picture_key } = this.props.singleProductCStore


    const prodQuantity = this.state.quantity
    const success = true


    return (
      //<!-- Document Wrapper -->
      <div className="">

        { loading ? (
            <div className='sweet-loading'>
              <div className='reverse-spinner'>
                <BeatLoader
                  color={'#FE980F'}
                  loading={loading}
                />
              </div>
            </div>)
          : ''
        }

        <div className="container single-product">
          <div className="row">
          <div className="col-xs-12 col-sm-12">
            {
              single_product ?
            (
            <div className="product-details">
              <div className="row" style={{ marginRight: 0, marginLeft: 0 }}>
                <div className="col-sm-2 thumbnail_master_body">
                  <div className="row thumnail_center">
                    { !_.isEmpty(single_product.varieties) ?
                      single_product.varieties[variety_id] ? (single_product.varieties[variety_id].pictures)
                        .map((val, key) => {
                          return (
                            <div className="col-4 variety_thumnail" key={key} onClick={ this._handleChangeVarietyImage.bind(this, key) }>
                              <div className={`variety_thumnail_opak ${ key==thumbnail_picture_key ? 'active' : 0 }`} key={key}>
                              </div>
                              <img className="" src={val} alt="" />
                            </div>
                          )
                        }) : null : null
                    }
                  </div>
                </div>
                <div className="col-sm-5">
                  <div className="view-product">
                    <div className="row">
                      { pic_loading ? (
                            <div className='spin'>
                              <RotateLoader
                                color={'#FE980F'}
                                loading={pic_loading}
                              />
                            </div>)
                        : ''
                      }

                      {/* IMAGE PREVISUALISATION VIEWER */}
                      <div className="single_product_img">
                        {/* Here the variety id must be set on picture */}
                        {/* <img className="" src={single_product.varieties ? single_product.varieties[variety_id].pictures[0] : null } alt="" /> */}
                        <img className="" src={single_product.varieties ? single_product.varieties[variety_id].pictures[thumbnail_picture_key] : null } alt="" />
                      </div>
                    </div>
                  </div>
                </div>
                <div className="col-sm-5 product_info_wrapper">
                  <div className="product-information">
                    <img src="images/product-details/new.jpg" className="newarrival" alt="" />
                    <h2 className="display-4">{ single_product.title }</h2>
                    <p>{'Ref: ' + single_product.ref }</p>

                    <h5 className="price-row">{ single_product.price + ' FCFA' }</h5>

                    <div className="row product-size" style={{ marginLeft: "0px", marginRight: "0px" }}>
                      <div className="col-sm-6" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                        <h6>Selectionner la taille</h6>
                        <p className="size">
                        { !_.isEmpty(single_product.varieties) ?
                          (single_product.varieties)
                            .map((val, key) => {
                              return (
                                <a href="#" key={key}>{val.size.name} &nbsp;</a>
                              )
                            }) : null
                        }
                        </p>
                      </div>
                      <div className="col-sm-6 link-size" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                        <a href="#" className="btn btn-link">Tableau tailles</a>
                      </div>
                    </div>

                    <form>
                      <div className="row color-and-qty" style={{ marginLeft: "0px", marginRight: "0px" }}>
                        <div className="col-sm-6 variety-color" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                          <div className="">
                            { !_.isEmpty(single_product.varieties) ?
                              (single_product.varieties)
                                .map((val, key) => {
                                  return (
                                    <div key={key} style={{ display: "inline-block" }}>
                                      <a
                                        href="#"
                                        onClick={this._handleChangeVariety.bind(this, key, val.quantity)}
                                        data-toggle="tooltip" data-placement="bottom" title={val.color.title}
                                        style={{ paddingRight: 5 }}
                                      >
                                        <img
                                          src={`${val.color.picture ? val.color.picture : null}`}
                                          width="30"
                                          height="30"
                                          style={{ borderRadius: 5 }}
                                        />
                                      </a>
                                    </div>
                                  )
                                }) : null
                            }
                          </div>
                        </div>

                        <div className="col-sm-6 cart_quantity_wrapper" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                          <div className="cart_quantity_button">
                            <button
                              type="button"
                              className="btn btn-light plusMinus"
                              onClick={this._handleRemoveQuantity.bind(this)}
                              disabled={ quantity == 1 || stock_quantity < 1 ?true:false }
                            >
                              -
                            </button>
                            <Field
                              className="cart_quantity_input"
                              component="input"
                              type="text"
                              name="quantity"
                              size="2"
                            />
                            <button
                              type="button"
                              className="btn btn-light plusMinus"
                              onClick={this._handleAddQuantity.bind(this)}
                              disabled={ quantity >= stock_quantity ?true:false }
                            >
                              +
                            </button>
                          </div>
                        </div>
                      </div>

                      <div className="row whishlist-and-cart" style={{ marginLeft: "0px", marginRight: "0px" }}>
                        <div className="col-sm-12 add-to-cart-wrapper" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                          <button
                            type="button"
                            className="btn btn-default cart full-cart"
                            onClick={this.props.handleSubmit( this._handleAddToCart.bind(this))}
                            disabled={ stock_quantity < 1 ?true:false }
                          >
                            <i className="fa fa-shopping-cart"></i>
                            &nbsp; Ajouter au panier
                          </button>
                        </div>
                        <div className="col-sm-12 add-to-cart-wrapper" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                          <button
                            type="button"
                            className="btn btn-default gift_btn full-cart"
                            onClick={this.props.handleSubmit( this._handleAddToCart.bind(this))}
                            disabled={ stock_quantity < 1 ?true:false }
                          >
                            <i className="fa fa-gift"></i>
                            &nbsp; Ajouter à ma box
                          </button>
                        </div>
                        <div className="col-sm-12 add-to-wishlist-wrapper" style={{ paddingLeft: "0px", paddingRight: "0px" }}>
                          <button
                            type="button"
                            className="btn btn-outline-secondary wishbutton"
                            style={{ width: "100%", marginBottom: 10 }}
                            onClick={this._handleAddToWhishList.bind(this)}
                          >
                            <i className="fa fa-heart"></i>
                            &nbsp; Mettre en favoris
                          </button>
                        </div>
                        <div style={{ paddingTop: "20px" }}>
                          <FacebookShareButton url={`https://github.com/stephcyrille`}>
                            <FacebookIcon size={32} round={true} />
                          </FacebookShareButton>
                          &nbsp;&nbsp;
                          <EmailShareButton url={`https://github.com/stephcyrille`}>
                            <EmailIcon size={32} round={true} />
                          </EmailShareButton>
                          &nbsp;&nbsp;
                          <WhatsappShareButton url={`https://github.com/stephcyrille`}>
                            <WhatsappIcon size={32} round={true} />
                          </WhatsappShareButton>
                        </div>
                      </div>
                    </form>

                    <div className="row description-resume">
                      <div className="col-sm-12">
                        <Collapse
                          bordered={false}
                          showArrow={false}
                          activeKey="1"
                          expandIconPosition="right"
                        >
                          <Panel header="Description" key="1">
                            {single_product.description}
                          </Panel>
                        </Collapse>
                      </div>
                    </div>

                  </div>
                </div>

                {/* The same Items block */}
              </div>
            </div>
            ):null

            }

          </div>
          </div>
        </div>


        <Dialog
          title={ "" }
          isOpen={ this.state.dialogOpen }
          onClose={ this.handleSetDialogClose.bind(this) }
          style={{ width: "350px" }}
        >
          <Paper style={{ padding: '2em' }}>
              <Grow
                in={success}
              >
                <div
                  style={{ transformOrigin: '0 0 0', width: 544 }}
                  {...(success ? { timeout: 1500 } : {})}
                >
                  <i className="far fa-check-circle fa-4x text-success" style={{ display: "block", textAlign: "center", marginBottom: 20 }}></i>
                  <h4 className="text-center" style={{ marginBottom: 20 }}>
                  { prodQuantity } { this.state.product ? this.state.product.title : "" }  bien ajouté au panier!</h4>
                  <div className={` mr-auto mx-auto`} style={{ textAlign: "center", marginTop: 20 }}>
                    <Button
                      onClick={ this.handleGotoCart.bind(this) }
                      className=""
                      variant="outlined"
                    >
                      Aller au panier
                    </Button>
                    &nbsp;
                    &nbsp;
                    <Button
                      onClick={ this.handleSetDialogClose.bind(this) }
                      className=""
                      variant="outlined"
                      color="primary"
                    >
                      continuer vos achats
                    </Button>
                  </div>
                </div>
              </Grow>

          </Paper>
        </Dialog>
      </div>
    );
  }
}
