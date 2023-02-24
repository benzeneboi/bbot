import { gql } from "@apollo/client";

export const CONSIDERATIONS_QUERY = gql `
  query ConsQuery {
    considerations {
      gameDateTime
      sport
      team1
      team2
      currDateTime
      betWindow
      timeDelta
    }
  }
`;