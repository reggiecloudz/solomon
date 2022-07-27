import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddDeviceComponent } from './device/components/add-device/add-device.component';
import { EditDeviceComponent } from './device/components/edit-device/edit-device.component';
import { ListDeviceComponent } from './device/components/list-device/list-device.component';
import { AddJobComponent } from './job/components/add-job/add-job.component';
import { EditJobComponent } from './job/components/edit-job/edit-job.component';
import { ListJobComponent } from './job/components/list-job/list-job.component';
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
  { path: 'jobs', component: ListJobComponent },
  { path: 'jobs/service-order/:id', component: AddJobComponent },
  { path: 'edit-job/:id', component: EditJobComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
