import { Component, OnInit } from '@angular/core';
import { Device } from '../../models/device.model';
import { DeviceService } from '../../services/device.service';

@Component({
  selector: 'app-list-device',
  templateUrl: './list-device.component.html',
  styleUrls: ['./list-device.component.css']
})
export class ListDeviceComponent implements OnInit {
  DeviceList: any = [];

  constructor(
    public deviceService: DeviceService
  ) { }

  ngOnInit(): void {
    this.loadDevices();
  }

  loadDevices() {
    return this.deviceService.GetClientDevices().subscribe((data: {}) => {
      this.DeviceList = data;
    });
  }

  // Delete device
  deleteDevice(data: any){
    var index = this.DeviceList.map((x: any) => {return x.brand}).indexOf(data.brand);
     return this.deviceService.DeleteDevice(data.id).subscribe(res => {
      this.DeviceList.splice(index, 1)
       console.log('Device deleted!')
     })
  }
}
