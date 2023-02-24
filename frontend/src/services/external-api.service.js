import { useQuery } from "@apollo/client";

export const CallExternalApi = (query) => {
    const { loading, error, data } = useQuery(query);
    console.log(loading, error, data);
}

/* import axios from 



const API_URL = "";

const makeQuery = (query, variables = {}) => {
    return axios.post(API_URL, {
        query,
        variables
    })
}

export const getData = async (query, variables = {}) => {
    try {
        const response = await makeQuery(query, variables);
        return response.data
    } catch (error) {
        console.error(error);
    }
} */