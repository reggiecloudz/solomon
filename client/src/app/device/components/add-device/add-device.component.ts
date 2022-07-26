import { Component, OnInit, NgZone } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

import { DeviceService } from '../../services/device.service';

@Component({
  selector: 'app-add-device',
  templateUrl: './add-device.component.html',
  styleUrls: ['./add-device.component.css']
})
export class AddDeviceComponent implements OnInit {

  deviceForm!: FormGroup;
  DeviceArr: any = [];

  ngOnInit() {
    this.addIssue();
  }
  constructor(
    public fb: FormBuilder,
    private ngZone: NgZone,
    private router: Router,
    public deviceService: DeviceService
  ) {}
  addIssue() {
    this.deviceForm = this.fb.group({
      brand: [''],
      model: [''],
      computer_type: [''],
    });
  }
  submitForm() {
    this.deviceService.CreateDevice(this.deviceForm.value).subscribe((res) => {
      console.log('Device added!');
      this.ngZone.run(() => this.router.navigateByUrl('/devices'));
    });
  }
}
