import { Component, OnInit, NgZone } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

import { DeviceService } from '../../services/device.service';

@Component({
  selector: 'app-edit-device',
  templateUrl: './edit-device.component.html',
  styleUrls: ['./edit-device.component.css']
})
export class EditDeviceComponent implements OnInit {
  DeviceList: any = [];
  updateDeviceForm!: FormGroup;

  ngOnInit(): void {
    this.updateForm();
  }

  constructor(
    private actRoute: ActivatedRoute,
    public deviceService: DeviceService,
    public fb: FormBuilder,
    private ngZone: NgZone,
    private router: Router
  ) {
    var id = this.actRoute.snapshot.paramMap.get('id');
    this.deviceService.GetDevice(Number(id)).subscribe((data) => {
      this.updateDeviceForm = this.fb.group({
        brand: [data.brand],
        model: [data.model],
        computer_type: [data.computer_type]
      });
    });
  }

  updateForm() {
    this.updateDeviceForm = this.fb.group({
      brand: [''],
      model: [''],
      computer_type: ['']
    });
  }

  submitForm() {
    var id = this.actRoute.snapshot.paramMap.get('id');
    this.deviceService.UpdateDevice(Number(id), this.updateDeviceForm.value).subscribe(res => {
      this.ngZone.run(() => this.router.navigateByUrl('/devices'));
    });
  }
}
