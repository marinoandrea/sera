const API_ENDPOINT = "https://sera-api.herokuapp.com";

export function generateQueryString(lang) {
  let out = API_ENDPOINT + "/audio/" + lang + "/search";
  out += "category=" + application.category + "&";
  out += "subcategory=" + application.subCategory + "&";
  out += "min_quantity=" + application.quantityLowerBound + "&";
  out += "max_quantity=" + application.quantityUpperBound;
  return out;
}
