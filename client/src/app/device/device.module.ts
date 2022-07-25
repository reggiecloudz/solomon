import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListDeviceComponent } from './components/list-device/list-device.component';
import { AddDeviceComponent } from './components/add-device/add-device.component';
import { EditDeviceComponent } from './components/edit-device/edit-device.component';
import { DeviceService } from './services/device.service';

@NgModule({
  declarations: [
    ListDeviceComponent,
    AddDeviceComponent,
    EditDeviceComponent
  ],
  providers: [DeviceService],
  imports: [
    CommonModule
  ]
})
export class DeviceModule { }
