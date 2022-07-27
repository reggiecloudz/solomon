import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddDeviceComponent } from './device/components/add-device/add-device.component';
import { EditDeviceComponent } from './device/components/edit-device/edit-device.component';
import { ListDeviceComponent } from './device/components/list-device/list-device.component';
import { AddServiceOrderComponent } from './service-order/components/add-service-order/add-service-order.component';
import { EditServiceOrderComponent } from './service-order/components/edit-service-order/edit-service-order.component';
import { ListServiceOrderComponent } from './service-order/components/list-service-order/list-service-order.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'add-device' },
  { path: 'add-device', component: AddDeviceComponent },
  { path: 'edit-device/:id', component: EditDeviceComponent },
  { path: 'devices', component: ListDeviceComponent },
  { path: 'devices/:id/service-orders', component: ListServiceOrderComponent },
  { path: 'devices/:id/add-service-order', component: AddServiceOrderComponent },
  { path: 'edit-service-order/:id', component: EditServiceOrderComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
