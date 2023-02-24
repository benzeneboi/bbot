import { useState } from "react";
import { Button, Typography, Box, IconButton } from "@mui/material";
import PowerSettingsNewOutlinedIcon from '@mui/icons-material/PowerSettingsNewOutlined';
import { fontWeight } from "@mui/system";

const Online = () => {
   return (
        <Typography sx={{color: "green", ml: "5px"}}>
            Online
        </Typography>
   ) 
}

const Offline = () => {
    return (
        <Typography sx={{color: "red", ml: "5px"}}>
            Offline
        </Typography>
    );
};


export const BotStatus = ({color}) => {
    const [status, setStatus] = useState(false);
    return (
        <Box width="100%" height="100%" m="0 30px"
          /* backgroundColor={color} *//* {colors.primary[400]} */
          /* display="flex"
          flexDirection="column" */
          /* alignItems="center" */
          /* justifyContent="center" */
          /* minWidth="150px" */
        >
            <Box display="flex" justifyContent="center">
            <IconButton color="secondary" onClick={() => setStatus(!status)}>
                <PowerSettingsNewOutlinedIcon sx={{ color: "grey", fontSize: "60px" }}/>
            </IconButton>
            </Box>

            <Box display="flex" justifyContent="center" mt="2px">
                <Typography>Bot Status:</Typography>
                {status ? <Online /> : <Offline />}
            </Box>
        </Box>
    );
};