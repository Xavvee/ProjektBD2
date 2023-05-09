import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OfferNavBarComponent } from './offer-nav-bar.component';

describe('OfferNavBarComponent', () => {
  let component: OfferNavBarComponent;
  let fixture: ComponentFixture<OfferNavBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OfferNavBarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OfferNavBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
