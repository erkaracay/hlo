"use client";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { FilterMatchMode } from 'primereact/api';
import { InputNumber } from 'primereact/inputnumber';
import { Tag } from 'primereact/tag';
import { Dropdown } from 'primereact/dropdown';
import { Button } from 'primereact/button';
import "primereact/resources/themes/lara-light-indigo/theme.css";
import "./stockmanagement.css"

function App() {
  const [data, setData] = useState([]);
  const [acc, setAcc] = useState([]);
  const [quantityMap, setQuantityMap] = useState({});
  const [filters, setFilters] = useState({
    type: { value: null, matchMode: FilterMatchMode.CONTAINS },
    urgency: { value: null, matchMode: FilterMatchMode.EQUALS }
  });
  const [urgencies] = useState([
    { label: 'LOW', value: 'LOW' },
    { label: 'MEDIUM', value: 'MEDIUM' },
    { label: 'HIGH', value: 'HIGH' },
  ]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/accaids?center=1")
      .then(response => {
        setData(response.data);
        const initialQuantityMap = {};
        response.data.forEach(item => {
          initialQuantityMap[item.id] = item.quantity;
        });
        setQuantityMap(initialQuantityMap);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
      
      axios.get("http://localhost:8000/api/acc/1/")
        .then(res => {
          setAcc(res.data);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
  }, []);

  const inputNumber = (rowData) => {
    const updateQuantity = (newValue) => {
      const updatedRow = { ...rowData, quantity: newValue };
      const newQuantityMap = { ...quantityMap };
      newQuantityMap[rowData.id] = newValue;
      setQuantityMap(newQuantityMap);
      return updatedRow;
    };
  
    const onSaveClick = () => {
      const updatedRowData = updateQuantity(quantityMap[rowData.id]);
      
      const apiUrl = `http://localhost:8000/api/accaids/${rowData.id}/`;
      
      axios.put(apiUrl, updatedRowData)
        .then(response => {
          console.log('Row Data saved:', response.data);
        })
        .catch(error => {
          console.error('Error saving Row Data:', error);
        });
    };
      
    return (
      <>
        <InputNumber
          value={quantityMap[rowData.id]}
          onValueChange={(e) => updateQuantity(e.value)}
          showButtons
          buttonLayout="horizontal"
          step={10}
          decrementButtonIcon="pi pi-minus"
          incrementButtonIcon="pi pi-plus"
        />
        <Button className="btnCheck ml-3" onClick={onSaveClick} icon="pi pi-check"></Button>
      </>
    );
  };
  

  const getSeverity = (urgency) => {
    switch (urgency) {
        case 'HIGH':
          return 'danger';
        case 'MEDIUM':
          return 'warning';
        case 'LOW':
          return 'success';
        default:
          return null;
    }
};

  const urgencyBodyTemplate = (rowData) => {
    return <Tag value={rowData.urgency} severity={getSeverity(rowData.urgency)} />;
  };
  
  const urgencyFilter = (options) => {
    if (!options) {
      return null;
    }
  
    return (
      <Dropdown
        value={options.value}
        options={urgencies}
        onChange={(e) => options.filterApplyCallback(e.value)}
        optionLabel="label"
        placeholder="Select One"
        className="p-column-filter"
        showClear
        style={{ minWidth: '12rem' }}
      />
    );
  };

  return (
    <>
      <div className="card">
        <DataTable value={data} emptyMessage="No data found" rows={10} dataKey="id" filters={filters} filterDisplay='row' showGridlines header={acc.name}>
          <Column field="type" header="Name" sortable filterMatchMode="contains" filter style={{ minWidth: '12rem' }} filterPlaceholder="Search by name" />
          <Column field="quantity" header="Quantity" body={inputNumber} />
          <Column field="urgency" header="Urgency" filter showFilterMenu={false} filterMenuStyle={{ width: '14rem' }}
          style={{ minWidth: '12rem' }} body={urgencyBodyTemplate} filterElement={urgencyFilter} />
        </DataTable>
      </div>
    </>
  );
}

export default App;
