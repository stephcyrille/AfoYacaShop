import React, { Component } from "react";
import { Button, TextField, Paper } from "@material-ui/core";
import Grow from '@material-ui/core/Grow';
import debounce from 'lodash.debounce'
import './style.local.css'


const items = []


export default
class HorizontalScroll extends Component {
  constructor() {
    super()

    this.state = {
      items: [...Array(10).keys()],
      hasOverflow: false,
      canScrollLeft: false,
      canScrollRight: false,

      dialogOpen: false,
      product: null,
      quantity: {
        value: 0,
        error: false,
        errorMessage: null,
      },
      // Toggle when adding on cart is a success
      success: false,
      products: [],
    }

    this.checkForOverflow = this.checkForOverflow.bind(this)
    this.checkForScrollPosition = this.checkForScrollPosition.bind(this)

    this.debounceCheckForOverflow = debounce(this.checkForOverflow, 1000)
    this.debounceCheckForScrollPosition = debounce(
      this.checkForScrollPosition,
      200
    )

    this.container = null
    this.handleSetDialogOpen = this.handleSetDialogOpen.bind(this);
  }

  _fetchProductFlashSale(){
    fetch('/api/list/products/flash_sales/'
      ,{
        headers : {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
      .then((res) => res.json())
      .then((res) => {
        this.setState({
          products: res
        });
      });
  }

  componentDidMount() {
    this.checkForOverflow()
    this.checkForScrollPosition()
    this._fetchProductFlashSale()

    this.container.addEventListener(
      'scroll',
      this.debounceCheckForScrollPosition
    )
  }

  componentWillUnmount() {
    this.container.removeEventListener(
      'scroll',
      this.debounceCheckForScrollPosition
    )
    this.debounceCheckForOverflow.cancel()
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.items.length !== this.state.items.length) {
      this.checkForOverflow()
      this.checkForScrollPosition()
    }
  }

  checkForScrollPosition() {
    const { scrollLeft, scrollWidth, clientWidth } = this.container

    this.setState({
      canScrollLeft: scrollLeft > 0,
      canScrollRight: scrollLeft !== scrollWidth - clientWidth
    })
  }

  checkForOverflow() {
    const { scrollWidth, clientWidth } = this.container
    const hasOverflow = scrollWidth > clientWidth

    this.setState({ hasOverflow })
  }

  scrollContainerBy(distance) {
    this.container.scrollBy({ left: distance, behavior: 'smooth' })
  }


  buildControls() {
    return (
      <div className="row" style={{ marginLeft: 0, marginRight: 0 }}>

          <div className="col-6">
              <h4 className="flash_sale">Ventes flash</h4>
          </div>


        <div className="col-6 item-controls">
          <i className="fa fa-chevron-left fa-2x chevron-lft"
            onClick={() => {
              this.scrollContainerBy(-200)
            }}
          ></i>


          <i className="fa fa-chevron-right fa-2x chevron-rgt"
            onClick={() => {
              this.scrollContainerBy(200)
            }}
          ></i>
        </div>
      </div>
    )
  }

  handleSetDialogOpen(event, element){
    event.preventDefault()
    this.setState({
      dialogOpen: true,
      product: element
    })
  }

  handleSetDialogClose(){
    this.setState({
      dialogOpen: false,
      product: null,
      success: false,
      quantity: {
        value: 0,
        error: false,
        errorMessage: null,
      }
    })
  }

  handleChangeQuantity(e){
    this.setState({
      quantity: e.target.value,
    })
  }

  handleSubmit(e){
    e.preventDefault()
    this.setState({
      quantity: e.target.quantity.value,
      success: true
    })
  }

  handleGotoCart(){
    window.location.href = `/`;
  }


  buildItems() {
    var products = this.state.products ? this.state.products : []

    return products.map((val, key) => {
      return (
        <li className="item" key={key}>
          <div className='showcase-whole-content'>
            <div className='showcase-pic-wrapper'>
              <a href={`/shop/products/women/single/${val.slug}`}>
                <img src={`${val.pictures[0]}`} className='' />
              </a>
            </div>
            <div className='showcase-pic-legend'>
              <h5 className="categories_home ttle" style={{ marginBottom: 5, paddingBottom: 5 }}>{val.title}</h5>
              <p>
                {/* The call list of products in the specific place */}
                <a href="" className="horizontal_scroll_country">Cameroun</a><br />
                {/*<a className="horizontal_scroll_add_to_cart" onClick={ this.handleSetDialogOpen.bind(this) }>Ajouter au panier</a> */}
              </p>
            </div>
          </div>
        </li>
      )
    })
  }


  render() {
    const { success, dialogOpen, quantity } = this.state

    return (
      <div className="scroll-body">
        <div className="scroll-wrapper">
          {this.buildControls()}
          <ul
            className="item-container"
            ref={node => {
              this.container = node
            }}
          >
            {this.buildItems()}
          </ul>
        </div>


      </div>
    );
  }
}

