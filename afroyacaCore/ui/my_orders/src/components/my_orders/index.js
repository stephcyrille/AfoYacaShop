import React from "react";
import { connect } from "react-redux";
import { PulseLoader } from 'react-spinners';
import Box from '@material-ui/core/Box';
import Collapse from '@material-ui/core/Collapse';
import IconButton from '@material-ui/core/IconButton';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableContainer from '@material-ui/core/TableContainer';
import TableRow from '@material-ui/core/TableRow';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
import _ from "underscore";

import { orderCStoreActions } from './store'
import { getUser } from '../../utils/auth_utils'
import './style.local.css';



function CustomRow(props) {
  const { row } = props;
  const [open, setOpen] = React.useState(false);

  return (
    <React.Fragment>
      <TableRow>
        <TableCell>
          <IconButton aria-label="expand row" size="small" onClick={() => setOpen(!open)}>
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell component="th" scope="row">
          Commande#{row.id}
        </TableCell>
        <TableCell align="right">{row.created_date ? new Date(row.created_date).toLocaleDateString() : null}</TableCell>
        <TableCell align="right">{row.delivery_date ? new Date(row.delivery_date).toLocaleDateString() : null}</TableCell>
        <TableCell align="right">{row.contact}</TableCell>
        <TableCell align="right">
          <span
            className={`badge ${row.status == 'confirmed' && 'badge-primary'} ${row.status == 'delivered' && 'badge-success'} ${row.status == 'pending' && 'badge-warning'} ${row.status == 'canceled' && 'badge-danger'}`}>
            {row.status}
          </span>
        </TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box margin={1}>
              <Typography variant="h6" gutterBottom component="div" style={{ paddingLeft: 20 }}>
                Contenu de la commande
              </Typography>
              <Table size="small" aria-label="purchases">
                <TableHead>
                  <TableRow>
                    <TableCell>Ref.</TableCell>
                    <TableCell>Nom du produit</TableCell>
                    <TableCell align="right">P.U</TableCell>
                    <TableCell align="right">Quantité</TableCell>
                    <TableCell align="right">Total ligne (FCFA)</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {row.products.map((productRow, key) => (
                    <TableRow key={key}>
                      <TableCell component="th" scope="row">
                        {productRow.ref}
                      </TableCell>
                      <TableCell>{productRow.title}</TableCell>
                      <TableCell align="right">{productRow.price}</TableCell>
                      <TableCell align="right">{productRow.quantity}</TableCell>
                      <TableCell align="right">
                        {Math.round(productRow.quantity * productRow.price * 100) / 100}
                      </TableCell>
                    </TableRow>
                  ))}
                  <TableRow>
                      <TableCell component="th" scope="row"></TableCell>
                      <TableCell></TableCell>
                      <TableCell align="right"></TableCell>
                      <TableCell align="right"><b style={{ fontSize: "1.31em" }}>Prix total</b></TableCell>
                      <TableCell align="right">
                        <b style={{ fontSize: "1.31em" }}>{row.products.reduce((a, v) => a=a+(v.quantity * v.price), 0)}</b>
                    </TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  );
}


const useStyles = theme => ({
  root: {
    paddingTop: 50,
    paddingBottom: 50,
  },
});




export default
@connect((state, props) => ({
  orderCStore: state.orderCStore
}))
class MyOrders extends React.Component {

  componentWillMount(){
    this.props.dispatch(orderCStoreActions.setLoading(true))

    this._fetchUserOrders()

    setTimeout(() => {
      this.props.dispatch(orderCStoreActions.setLoading(false))
    }, 2000);
  }

  _fetchUserOrders(){
    const user_id = getUser() ? getUser().userprofile.id : null
    const service = `orders?user=${user_id}`
    const url = `api/account/my/orders`

    window.axios
    .get(`${url}`)
    .then(response => {
      var orders = response.data
      this.props.dispatch(orderCStoreActions.setOrders(orders))
    })
    .catch(
      error => {
        console.error("Errrorr", error)
      }
    )
  }




  render() {
    const { loading, orders } = this.props.orderCStore

    return (
      //<!-- Document Wrapper -->
      <div className="" style={{ backgroundColor: "white" }}>
          <div className="container">
            <h3 className="text-center" style={{ marginBottom: 20 }}>Mes commandes</h3>
            <div>
              <TableContainer component={Paper}>
                <Table aria-label="collapsible table">
                  <TableHead>
                    <TableRow>
                      <TableCell />
                      <TableCell>Reférence</TableCell>
                      <TableCell align="right">Date de commande</TableCell>
                      <TableCell align="right">Date d'arrivée</TableCell>
                      <TableCell align="right">Adresse</TableCell>
                      <TableCell align="right">Status</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {orders.map((row, key) => (
                      <CustomRow key={key} row={row} />
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </div>
          </div>

      </div>
    );
  }
}
