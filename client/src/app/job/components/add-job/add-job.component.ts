import { Component, OnInit, NgZone } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { JobService } from '../../services/job.service';
import users from '../../../shared/users';

@Component({
  selector: 'app-add-job',
  templateUrl: './add-job.component.html',
  styleUrls: ['./add-job.component.css']
})
export class AddJobComponent implements OnInit {
  orderId = this.actRoute.snapshot.paramMap.get('id');
  jobForm!: FormGroup;
  JobArr: any = [];

  ngOnInit() {
    this.addJob();
  }
  constructor(
    private actRoute: ActivatedRoute,
    public fb: FormBuilder,
    private ngZone: NgZone,
    private router: Router,
    public jobService: JobService
  ) {}
  addJob() {
    this.jobForm = this.fb.group({
      label: [''],
    });
  }
  submitForm() {
    this.jobService.CreateJob(this.jobForm.value, Number(this.orderId)).subscribe((res) => {
      console.log('Job added!');
      this.ngZone.run(() => this.router.navigateByUrl('/jobs'));
    });
  }
}
