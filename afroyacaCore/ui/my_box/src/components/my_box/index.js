import React from "react";
import { connect } from "react-redux";
import { PulseLoader } from 'react-spinners';
import MaterialTable from "material-table";
import { Add as AddIcon } from "@material-ui/icons";
import _ from "underscore";

import tableIcons from "./TableIcon";
import { myBoxCStoreActions } from './store'
import style from './style.local.scss';


export default
@connect((state, props) => ({
  myBoxCStore: state.myBoxCStore
}))
class MyBox extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      data: [
        {
          id: 1,
          picture: "/media/products/vetements/variety/robe-imprimee-floral",
          product: "Robe fleuri",
          price: 20000
        },
        {
          id: 2,
          picture: "/media/main_menu_nav/bagg.jpg",
          product: "Sac à main Jaydee",
          price: 15000
        }
      ],
      categories_data: [],

      snack_open: false,
      snack_message: null,
      snack_color: null,
    }
  }


  componentWillMount(){
    this.props.dispatch(myBoxCStoreActions.setLoading(true))

    this._fetchUserOrders()

    setTimeout(() => {
      this.props.dispatch(myBoxCStoreActions.setLoading(false))
    }, 2000);
  }

  _fetchUserOrders(){
    const url = `api/account/my/box`

    window.axios
    .get(`${url}`)
    .then(response => {
      var box = response.data
      this.props.dispatch(myBoxCStoreActions.setBox(box))
    })
    .catch(
      error => {
        console.error("Errrorr", error)
      }
    )
  }


  handleDeleteRow(oldData){
    this.setState((prevState) => {
      const datas = [...prevState.datas];
      datas.splice(datas.indexOf(oldData), 1);
      return { ...prevState, datas };
    })
  }

  renderTotalAmount = () => {
    return (
      <h5>Montant total : 120000FCFA</h5>
    )
  }




  render() {
    const { classes } = this.props
    const { loading, box } = this.props.myBoxCStore
    const columns = [
      { title: 'N°', field: 'id' },
      {
        title: 'Photo',
        field: 'picture',
        render: rowData => <img src={rowData.picture} style={{ width: 140, height: 180 }} />
      },
      { title: 'Nom du produit', field: 'product' },
      {
        title: 'Prix',
        field: 'price',
        render: rowData => <span>{rowData.price} FCFA</span>
      },
    ];
    const title = this.renderTotalAmount()

    const actions = [
      {
        icon: () => <AddIcon />,
        tooltip: 'Ajouter un produit',
        isFreeAction: true,
        onClick: (event, rowData) => {
          this.handleSetDialogOpen();
        },
      },
    ];

    return (
      //<!-- Document Wrapper -->
      <div className="" style={{ backgroundColor: "white" }}>
        <div className="container">
          <h3 className="text-center" style={{ marginBottom: 40, textTransform: "uppercase" }}>Ma box</h3>

          <section>
            <MaterialTable
              data={this.state.data}
              columns={columns}
              actions={actions}
              title={title}
              icons={tableIcons}
              editable={{
                onRowDelete: (oldData) =>
                  new Promise((resolve) => {
                    setTimeout(() => {
                      resolve();
                      this.handleDeleteRow(oldData)
                    }, 600);
                  }),
              }}
              options={{
                actionsColumnIndex: -1
              }}
            />
          </section>
        </div>
      </div>
    );
  }
}
