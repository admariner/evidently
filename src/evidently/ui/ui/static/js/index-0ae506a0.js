import{W as i,i as n,z as m,d as r,j as t,G as c}from"./vendor-22c0ce7a.js";import{D as d}from"./DashboardContent-f5b5bd51.js";import{u as p,D as j}from"./index-1612fd75.js";import"./createSvgIcon-6a7b5fca.js";import"./Edit-5db35e51.js";const g=()=>{const{projectId:e}=i();n(e,"missing projectId");const a=m(),s={minDate:r(a.min_timestamp),maxDate:r(a.max_timestamp)},{isCorrectTimeInterval:o}=p({dataRanges:s});return t.jsxs(t.Fragment,{children:[t.jsx(j,{dataRanges:s}),o&&t.jsx(c,{container:!0,spacing:3,direction:"row",alignItems:"stretch",children:t.jsx(d,{info:a})})]})};export{g as Component};