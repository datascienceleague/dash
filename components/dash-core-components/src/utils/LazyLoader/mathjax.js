export default () => Promise.resolve(window.MathJax ||
    import(/* webpackChunkName: "mathjax" */ 'mathjax-full/components/src/tex-svg/tex-svg.js').then(() => {
        window.MathJax.config.startup.typeset = false;

        return window.MathJax;
    })
);
