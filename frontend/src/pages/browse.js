import * as React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {
    Grid,
    Card,
    CardContent,
    Typography,
    CardHeader
  } from "@material-ui/core/";

  const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      padding: theme.spacing(2)
    }
  }));
  

const Browse = () => {
    const classes = useStyles();
    const data = {
        name: [
          { type: "Feel-Good" },
          { type: "Action/Thriller" },
          { type: "Comedy" },
          { type: "Sad" },
          { type: "Upbeat" },
          { type: "Calming" }
        ],
        id: [1]
      };

    return (
        <div className={classes.root}>
      {data.id.map((elem) => (
        <Grid
          container
          spacing={2}
          direction="row"
          justify="flex-start"
          alignItems="flex-start"
        >
          {data.name.map((elem) => (
            <Grid item xs={3} key={data.name.indexOf(elem)}>
              <Card>
                <CardHeader
                  title={` ${elem.type}`}
                />
                <CardContent>
                  <Typography variant="h5" gutterBottom>
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      ))}
    </div>
    )
}

export default Browse;


