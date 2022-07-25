import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddDeviceComponent } from './device/components/add-device/add-device.component';
import { EditDeviceComponent } from './device/components/edit-device/edit-device.component';
import { ListDeviceComponent } from './device/components/list-device/list-device.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'add-device' },
  { path: 'add-device', component: AddDeviceComponent },
  { path: 'edit-device/:id', component: EditDeviceComponent },
  { path: 'devices', component: ListDeviceComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
