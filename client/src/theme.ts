import { extendTheme } from "@chakra-ui/react";

const colors = {
  bg: "#ECEFF4",
  fg: "#D8DEE9",
  brand: "#8FBCBB",
  text: "#2E3440",
  success: { dark: "#10B981", light: "#D1FAE5" },
  error: { light: "#FEE2E2", dark: "#EF4444" },
  info: { dark: "#3B82F6", light: "#DBEAFE" },
  warn: { dark: "#da9100", light: "#FEF3C7" },
};

const styles = {
  global: {
    "html, body": {
      backgroundColor: "bg",
    },
  },
};

const theme = extendTheme({ colors, styles });

export default theme;
