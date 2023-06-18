import { TestBed } from '@angular/core/testing';

import { MakingReservationService } from './making-reservation.service';

describe('MakingReservationService', () => {
  let service: MakingReservationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MakingReservationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
