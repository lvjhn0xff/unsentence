import Mithril from "mithril";

export const m = Mithril

export const asyncComponent = (importComponent) => {
  let component = null;
  return {
    oninit: () => {
      importComponent().then(loaded => {
        component = loaded.default;
        m.redraw(); // Re-render after component loads
      });
    },
    view: () => component ? m(component) : m("div", "Loading...")
  };
};
