import { Box, Grid, Button, IconButton, Typography, useTheme, useMediaQuery } from "@mui/material";
import { tokens } from "../../theme";
import { mockTransactions } from "../../data/mockData";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import EmailIcon from "@mui/icons-material/Email";
import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import TrafficIcon from "@mui/icons-material/Traffic";
import Header from "../../components/Header";
import LineChart, { LineChart2 } from "../../components/LineChart";
import GeographyChart from "../../components/GeographyChart";
import BarChart from "../../components/BarChart";
import StatBox from "../../components/StatBox";
import ProgressCircle from "../../components/ProgressCircle";
import PowerSettingsNewOutlinedIcon from '@mui/icons-material/PowerSettingsNewOutlined';


import { CallExternalApi } from "../../services/external-api.service";
import { CONSIDERATIONS_QUERY } from "../../services/queries";
import { useLazyQuery, useQuery } from "@apollo/client";
import { BotStatus } from "../../components/BotStatus";
import { DataGrid } from "@mui/x-data-grid";
import { color } from "@mui/system";
import FlexBetween from "../../components/FlexBetween";


const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const isNonMediumScreens = useMediaQuery("(min-width: 1200px)");
  /* const { data, isLoading } = useGetDashboardQuery(); */

  
  const [getConsiderations, { loading, error, data }] = useLazyQuery(CONSIDERATIONS_QUERY);
  
  if (data) {
    console.log('using lazy query')
    console.log(data.considerations);
  }

  const columns = [
    {field: 'sport', headerName: 'Sport'},
    {field: 'team1', headerName: 'Team 1'},
    {field: 'team2', headerName: 'Team 2'},
    {field: 'currDateTime', headerName: 'Current Date'},
    {field: 'gameDateTime', headerName: 'Game Date'},
    {field: 'timeDelta', headerName: 'Delta Time'},
    {field: 'betWindow', headerName: 'Bet Window'},
  ];

  return (
    
    <Box m="1.5rem 2.5rem">
      {data && 
      <DataGrid 
        rows={data.considerations}
        columns={columns} 
      />}
      {/* <Grid container>
        <Grid item>a</Grid>
        <Grid item>b</Grid>
        <Grid item>c</Grid>
        <Grid item>d</Grid>
      </Grid> */}
      {/* <FlexBetween>
      <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />

      <Box>
        <Button
          onClick={() => {getConsiderations()}}
          sx={{
            backgroundColor: colors.blueAccent[700],
            color: colors.grey[100],
            fontSize: "14px",
            fontWeight: "bold",
            padding: "10px 20px",
          }}
        >
          <DownloadOutlinedIcon sx={{ mr: "10px" }} />
          Download Reports
        </Button>
      </Box>
      </FlexBetween> */}

      <Grid container justifyContent="space-between">
        <Grid item xs={12} sm={3}>
        <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />
        </Grid>
        <Grid item xs={12} sm={3}>
          <Box
            display="flex"
            justifyContent="right"
          >
            {/* NOTE: Testing GQL API query */}
            <Button
              onClick={() => {getConsiderations()}}
              sx={{
                backgroundColor: colors.blueAccent[700],
                color: colors.grey[100],
                fontSize: "14px",
                fontWeight: "bold",
                padding: "10px 20px",
              }}
            >
              <DownloadOutlinedIcon sx={{ mr: "10px" }} />
              Download Reports
            </Button>
          </Box>
        </Grid>
      </Grid>

      <Grid container spacing={2} /* rowSpacing={2} columnSpacing={2} */ justifyContent="center" /* alignItems="center" */>
        <Grid item xs={12} sm={6} md={3} xl={3}>
          <Box display="flex" alignItems="center" p="10px 0 10px 0">
            <BotStatus color={colors.primary[400]}/>
          </Box>
        </Grid>
        <Grid item xs={12} sm={6} md={3} xl={3} /* backgroundColor={colors.primary[400]} */>
          <Box
          display="flex"
          height="100%"
          alignItems="center"
          backgroundColor={colors.primary[400]}
          p="10px 0 10px 0"
          >
          
          <StatBox
            title="12,361"
            subtitle="Emails Sent"
            progress="0.75"
            increase="+14%"
            icon={
              <EmailIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
          </Box>{/* <BotStatus /> */}</Grid>
        <Grid item xs={12} sm={6} md={3} xl={3}>
          <Box
            display="flex"
            height="100%"
            alignItems="center"
            backgroundColor={colors.primary[400]}
            p="10px 0 10px 0"
          >
            <StatBox
                title="32,441"
                subtitle="New Clients"
                progress="0.30"
                increase="+5%"
                icon={
                  <PersonAddIcon
                    sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
                  />
                }
              />
          </Box>
        </Grid>
        <Grid item xs={12} sm={6} md={3} xl={3}><BotStatus /></Grid>
        
        {/* Line Chart */}
        <Grid item xs={12} sm={12} md={7.5} xl={12}>
          {/* <BotStatus /> */}
          <Box
          /* display="flex" */
          backgroundColor={colors.primary[400]}
          /* display="flex"
          flexDirection="column"
          alignItems="space-between" */

          >
            <Box
              /* mt="25px" */
              p="0 30px"
              display="flex"
              justifyContent="space-between"
              alignItems="center"
            >
              <Box>
                <Typography
                  variant="h5"
                  fontWeight="600"
                  color={colors.grey[100]}
                >
                  Net Return{/* Revenue Generated */}
                </Typography>
                <Typography
                  variant="h3"
                  fontWeight="bold"
                  color={colors.greenAccent[500]}
                >
                  $59,342.32
                </Typography>
              </Box>
              <Box>
                <IconButton>
                  <DownloadOutlinedIcon
                    sx={{ fontSize: "26px", color: colors.greenAccent[500] }}
                  />
                </IconButton>
              </Box>
            </Box>
              <Box display="flex" height="350px" m="0 0 0 0"/* "-20px -60px 0 0" */>
                {/* <LineChart isDashboard={true} /> */}
                <LineChart2 />
              </Box>
          </Box>
        </Grid>

        {/* Table data */}
        <Grid item xs={12} sm={12} md={4.5} xl={12}>
          {/* <BotStatus /> */}
          <Box
          backgroundColor={colors.primary[400]}
          height="400px"

          /* display="flex"
          flexDirection="column" */
          overflow="auto"
          >
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            borderBottom={`4px solid ${colors.primary[500]}`}
            colors={colors.grey[100]}
            p="15px"
          >
            <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
              Recent Transactions
            </Typography>
          </Box>
          {mockTransactions.map((transaction, i) => (
            <Box
              key={`${transaction.txId}-${i}`}
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              borderBottom={`4px solid ${colors.primary[500]}`}
              p="15px"
            >
              <Box>
                <Typography
                  color={colors.greenAccent[500]}
                  variant="h5"
                  fontWeight="600"
                >
                  {transaction.txId}
                </Typography>
                <Typography color={colors.grey[100]}>
                  {transaction.user}
                </Typography>
              </Box>
              <Box color={colors.grey[100]}>{transaction.date}</Box>
              <Box
                backgroundColor={colors.greenAccent[500]}
                p="5px 10px"
                borderRadius="4px"
              >
                ${transaction.cost}
              </Box>
            </Box>
          ))}
        </Box>
        </Grid>
      </Grid>


      {/* HEADER */}
      
      <FlexBetween>
        <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />

        <Box>
          {/* NOTE: Testing GQL API query */}
          <Button
            onClick={() => {getConsiderations()}}
            sx={{
              backgroundColor: colors.blueAccent[700],
              color: colors.grey[100],
              fontSize: "14px",
              fontWeight: "bold",
              padding: "10px 20px",
            }}
          >
            <DownloadOutlinedIcon sx={{ mr: "10px" }} />
            Download Reports
          </Button>
        </Box>
      </FlexBetween>

      
    </Box>
  );
};

export default Dashboard;
