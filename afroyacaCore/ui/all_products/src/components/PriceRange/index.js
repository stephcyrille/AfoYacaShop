import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';
import { createMuiTheme } from '@material-ui/core/styles'
import { ThemeProvider } from '@material-ui/styles';


const theme = createMuiTheme({
  overrides:{
    MuiSlider: {
      thumb:{
      color: "#ddaa44",
      },
      track: {
        color: '#000'
      },
      rail: {
        color: 'greay'
      }
    }
  },
  aydmain: {
    // Purple and green play nicely together.
    main: '#ddaa44'
  },
  ayddark: {
    // This is green.A700 as hex.
    main: '#8a6314',
  },
});

const useStyles = makeStyles({
  root: {
    width: "100%",
    padding: "40px 10px 10px 10px",
  },
});


function valuetext(value) {
  return `${value} k`;
}

export default function RangeSlider(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState([1, 30]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div>
      <ThemeProvider theme={theme}>
        <span style={{ fontSize: "1.2em" }} >De { value[0] * 1000 } à { value[1] * 1000 } FCFA</span><br/>
        <div className={classes.root}>
          <Slider
            value={value}
            onChange={handleChange}
            getAriaValueText={valuetext}
            aria-labelledby="range-slider"
            valueLabelDisplay="on"
            step={props.step?props.step:10}
            marks={props.marks}
            colorPrimary="aydmain"
          />
        </div>
      </ThemeProvider>
    </div>
  );
}
