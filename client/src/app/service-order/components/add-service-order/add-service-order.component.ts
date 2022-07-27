import { Component, OnInit, NgZone } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { ServiceOrderService } from '../../services/service-order.service';

@Component({
  selector: 'app-add-service-order',
  templateUrl: './add-service-order.component.html',
  styleUrls: ['./add-service-order.component.css']
})
export class AddServiceOrderComponent implements OnInit {
  deviceId = this.actRoute.snapshot.paramMap.get('id');
  serviceOrderForm!: FormGroup;
  ServiceOrderArr: any = [];

  ngOnInit() {
    this.addServiceOrder();
  }

  constructor(
    private actRoute: ActivatedRoute,
    public fb: FormBuilder,
    private ngZone: NgZone,
    private router: Router,
    public serviceOrderService: ServiceOrderService
  ) { }

  addServiceOrder() {
    this.serviceOrderForm = this.fb.group({
      problem: ['']
    });
  }

  submitForm() {
    this.serviceOrderService.CreateServiceOrder(this.serviceOrderForm.value, Number(this.deviceId)).subscribe((res) => {
      console.log('Service Order added!');
      this.ngZone.run(() => this.router.navigateByUrl(`devices/${this.deviceId}/service-orders`));
    });
  }

}
