import { ResponsiveLine } from "@nivo/line";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";
import { mockLineData2 as data } from "../data/mockData";

import { Line } from "@nivo/line";


const LineChart = ({ isCustomLineColors = false, isDashboard = false }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    

    
    <ResponsiveLine
      
      data={data}
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
        tooltip: {
          container: {
            color: colors.primary[500],
          },
        },
      }}
      colors={isDashboard ? { datum: "color" } : { scheme: "nivo" }} // added
      margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
      xScale={{ type: 'point' }}
      yScale={{
        type: "linear",
        min: "auto",
        max: "auto",
        stacked: true,
        reverse: false,
      }}
      yFormat=" >-.2f"
      curve=/* "catmullRom" */ "linear"
      axisTop={null}
      axisRight={null}
      axisBottom={{
        orient: "bottom",
        tickSize: 0,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "transportation", // added
        legendOffset: 36,
        legendPosition: "middle",
      }}
      axisLeft={{
        orient: "left",
        tickValues: 5, // added
        tickSize: 3,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "count", // added
        legendOffset: -40,
        legendPosition: "middle",
      }}
      enableGridX={false}
      enableGridY={false}
      pointSize={8}
      pointColor={{ theme: "background" }}
      pointBorderWidth={2}
      pointBorderColor={{ from: "serieColor" }}
      pointLabelYOffset={-12}
      useMesh={true}
      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 100,
          translateY: 0,
          itemsSpacing: 0,
          itemDirection: "left-to-right",
          itemWidth: 80,
          itemHeight: 20,
          itemOpacity: 0.75,
          symbolSize: 12,
          symbolShape: "circle",
          symbolBorderColor: "rgba(0, 0, 0, .5)",
          effects: [
            {
              on: "hover",
              style: {
                itemBackground: "rgba(0, 0, 0, .03)",
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
    />
  );
};

export default LineChart;

export const LineChart2 = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
  <ResponsiveLine
      
      
      data={[
          {
              id: 'positive :)',
              data: [
                  { x: 0, y: 0.7 },
                  { x: 1, y: 0.9 },
                  { x: 2, y: 0.8 },
                  { x: 3, y: 0.6 },
                  { x: 4, y: 0.3 },
                  { x: 5, y: 0 },
                  { x: 6, y: null },
                  { x: 7, y: null },
                  { x: 8, y: null },
                  { x: 9, y: null },
                  { x: 10, y: null },
                  { x: 11, y: 0 },
                  { x: 12, y: 0.4 },
                  { x: 13, y: 0.6 },
                  { x: 14, y: 0.5 },
                  { x: 15, y: 0.3 },
                  { x: 16, y: 0.4 },
                  { x: 17, y: 0 },
              ],
          },
          {
              id: 'negative :(',
              data: [
                  { x: 5, y: 0 },
                  { x: 6, y: -0.3 },
                  { x: 7, y: -0.5 },
                  { x: 8, y: -0.9 },
                  { x: 9, y: -0.2 },
                  { x: 10, y: -0.4 },
                  { x: 11, y: 0 },
                  { x: 12, y: null },
                  { x: 13, y: null },
                  { x: 14, y: null },
                  { x: 15, y: null },
                  { x: 16, y: null },
                  { x: 17, y: 0 },
                  { x: 18, y: -0.4 },
                  { x: 19, y: -0.2 },
                  { x: 20, y: -0.1 },
                  { x: 21, y: -0.6 },
              ],
          },
      ]}
      theme={{
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
              strokeWidth: 1,
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
        tooltip: {
          container: {
            color: colors.primary[500],
          },
        },
      }}
      margin={{ top: 50, right: 40, bottom: 50, left: 60 }}
      /* curve={select('curve', curveOptions, 'monotoneX')} */
      enablePointLabel={false}
      /* pointSymbol={CustomSymbol} */
      pointSize={10}
      pointBorderWidth={1}
      pointBorderColor={{
          from: 'color',
          modifiers: [['darker', 0.3]],
      }}
      
      pointLabelYOffset={-20}
      
      enableGridX={false}
      enableGridY={false}
      
      colors={['rgb(97, 205, 187)', 'rgb(244, 117, 96)']}
      xScale={{
          type: 'linear',
      }}
      yScale={{
          type: 'linear',
          stacked: false,
          min: -1,
          max: 1,
      }}
      enableArea={true}
      areaOpacity={0.07}
      enableSlices={false}
      useMesh={true}
      crosshairType="cross"
      
      axisLeft={{
        orient: "left",
        tickValues: 5, // added
        tickSize: 3,
        tickPadding: 5,
        tickRotation: 0,
        legend: undefined, // added
        legendOffset: -40,
        legendPosition: "middle",
      }}
      axisBottom={{
        orient: "bottom",
        tickSize: 0,
        tickPadding: 5,
        tickRotation: 0/* ,
        legend: undefined,/// added
        legendOffset: 36,
        legendPosition: "middle", */
      }}
      
  />
)
    }