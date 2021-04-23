import { Service } from "use-http-service";
import { API_ENDPOINT } from "../config";
import { Offering, SuccessResponse, User } from "../types";

const ROUTE = `${API_ENDPOINT}/offerings`;

export const OfferingsAPI = {
  buildGetOfferingsLatest: (): Service => ({
    url: `${ROUTE}/latest`,
    method: "GET",
  }),

  buildPostOfferingsSearch: (): Service => ({
    url: `${ROUTE}/search`,
    method: "POST",
  }),
};

export default OfferingsAPI;

export type GetOfferingsLatestRequest = unknown;
export type GetOfferingsLatestResponse = SuccessResponse<{
  offerings: Offering[];
  users: User[];
}>;

export type PostOfferingsSearchRequest = {
  category: string;
  subcategory: string;
  min_quantity?: number;
  max_quantity?: number;
};
export type PostOfferingsSearchResponse = SuccessResponse<{
  offerings: Offering[];
  users: User[];
}>;
