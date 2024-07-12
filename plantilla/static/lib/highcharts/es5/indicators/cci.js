!/**
 * Highstock JS v11.4.3 (2024-05-22)
 *
 * Indicator series type for Highcharts Stock
 *
 * (c) 2010-2024 Sebastian Bochan
 *
 * License: www.highcharts.com/license
 */function(t){"object"==typeof module&&module.exports?(t.default=t,module.exports=t):"function"==typeof define&&define.amd?define("highcharts/indicators/cci",["highcharts","highcharts/modules/stock"],function(e){return t(e),t.Highcharts=e,t}):t("undefined"!=typeof Highcharts?Highcharts:void 0)}(function(t){"use strict";var e=t?t._modules:{};function n(t,e,n,o){t.hasOwnProperty(e)||(t[e]=o.apply(null,n),"function"==typeof CustomEvent&&window.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:e,module:t[e]}})))}n(e,"Stock/Indicators/CCI/CCIIndicator.js",[e["Core/Series/SeriesRegistry.js"],e["Core/Utilities.js"]],function(t,e){var n,o=this&&this.__extends||(n=function(t,e){return(n=Object.setPrototypeOf||({__proto__:[]})instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)}),r=t.seriesTypes.sma,i=e.isArray,s=e.merge,u=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return o(e,t),e.prototype.getValues=function(t,e){var n,o,r,s,u,c,a,p=e.period,f=t.xData,h=t.yData,l=h?h.length:0,d=[],y=[],g=[],m=[],v=[],_=1;if(!(f.length<=p)&&i(h[0])&&4===h[0].length){for(;_<p;)o=h[_-1],d.push((o[1]+o[2]+o[3])/3),_++;for(a=p;a<=l;a++)u=((o=h[a-1])[1]+o[2]+o[3])/3,r=d.push(u),s=(v=d.slice(r-p)).reduce(function(t,e){return t+e},0)/p,c=function(t,e){var n,o=t.length,r=0;for(n=0;n<o;n++)r+=Math.abs(e-t[n]);return r}(v,s)/p,n=(u-s)/(.015*c),y.push([f[a-1],n]),g.push(f[a-1]),m.push(n);return{values:y,xData:g,yData:m}}},e.defaultOptions=s(r.defaultOptions,{params:{index:void 0}}),e}(r);return t.registerSeriesType("cci",u),u}),n(e,"masters/indicators/cci.src.js",[e["Core/Globals.js"]],function(t){return t})});